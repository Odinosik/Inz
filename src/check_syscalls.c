#include <asm/asm-offsets.h>
#include <linux/kernel.h>

#include "core.h"
#include "check_modules.h"
#include "check_syscalls.h"

//Analiza wywolan systemowych

void analyze_syscalls(void){
	struct module *mod;
	unsigned long **sys_call_table;
	unsigned long **interrupt_table;
	int (*core_kernel_text)(unsigned long addr) = NULL;
	int sysCount = NR_syscalls;
	int interupt_count = 256;
	int sysHooked = 0;
	int i = 0;
	int interruptHooked = 0;

	sys_call_table = (void *)kallsyms_lookup_name("sys_call_table");
	core_kernel_text = (void *)kallsyms_lookup_name("core_kernel_text");


	if (!sys_call_table) {
		printk("Blad --- nie znaleziono tablicy wywolan systemowych");
		return;
	}

	if(!core_kernel_text) {
		printk("Blad --- nie znaleziono funkcji core_kernel_text");
		return;
		}

	for (i = 0; i < sysCount; i++){
		if (!core_kernel_text((unsigned long)sys_call_table[i]))
		{
		mutex_lock(&module_mutex);
		mod = __module_address((unsigned long)sys_call_table[i]);
		if (mod)
		{
			printk("Przechwycone wywolanie systemowe numer %d  przez modul %s.\n", i, mod->name);
			sysHooked += 1;
		}
		else
		{
			printk("Przechwycone wywolanie systemowe numer %d  o adresie %lu  \n", i, (unsigned long)sys_call_table[i]);
			sysHooked += 1;
		}
		mutex_unlock(&module_mutex);
		}
	}

	printk("Liczba przechwyconych wywolan %d \n", sysHooked);


	i = 0;

	interrupt_table = (void *)kallsyms_lookup_name("idt_table");


	if (!interrupt_table) {
		printk("Blad --- nie znaleziono tablicy przerywan");
		return;
	}

	if(!core_kernel_text) {
		printk("Blad --- nie znaleziono funkcji core_kernel_text");
		return;
		}
	for (i = 0; i < interupt_count; i++){
		if (core_kernel_text((unsigned long)interrupt_table[i]))
		{
		mutex_lock(&module_mutex);
		mod = __module_address((unsigned long)interrupt_table[i]);
		if (mod)
		{
			printk("Przechwycone przerywanie numer %d  przez modul %s.\n", i, mod->name);
			interruptHooked += 1;
		}
		else
		{
			printk("Przechwycone przerywanie numer %d  o adresie %lu  \n", i, (unsigned long)interrupt_table[i]);
			interruptHooked += 1;
		}
		mutex_unlock(&module_mutex);
		}
	}
	printk("Liczba przechwyconych przerywan %d \n", interruptHooked);
}
