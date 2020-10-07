SRCDIR := src

obj-m := Main.o
Main-y += $(SRCDIR)/core.o
Main-y += $(SRCDIR)/check_modules.o
Main-y += $(SRCDIR)/check_syscalls.o

HEADERS := $(PWD)/include
ccflags-y += -I$(HEADERS)
module:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean-module:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
