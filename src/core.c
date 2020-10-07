#include "core.h"
#include "check_modules.h"
#include "check_syscalls.h"

static int __init init_mod(void){
	printk("Uruchomienie modulu\n");
	analyze_modules();
	analyze_syscalls();
	return 0;
}

static void __exit exit_mod(void){
	printk("Koniec dzialania modulu\n");
}

MODULE_LICENSE("GPL");

module_init(init_mod);
module_exit(exit_mod);
