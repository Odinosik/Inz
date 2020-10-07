#include "core.h"
#include "check_modules.h"

void analyze_modules(void){
	struct kset *mod_kset;
	struct kobject *cur, *tmp;
	struct module_kobject *kobj;
	int modHidden = 0;

	mod_kset = (void *)kallsyms_lookup_name("module_kset");
	if (!mod_kset){
		printk("Nie znaleziono symbolu");
		}

	list_for_each_entry_safe(cur, tmp, &mod_kset->list, entry){
		if (!kobject_name(tmp)) {
      break;
    }
		kobj = container_of(tmp, struct module_kobject, kobj);

		if (kobj && kobj->mod && kobj->mod->name){
			mutex_lock(&module_mutex);

			if(!find_module(kobj->mod->name)) {
				printk("Modul ukryty o nazwie %s \n", kobj->mod->name);\
				modHidden += 1;
			}
			mutex_unlock(&module_mutex);
		}
	}
	printk("Liczba wykrytych modulow %d\n", modHidden);
}
