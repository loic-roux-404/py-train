MODULES:=$(patsubst env.%,%,$(wildcard env.*))

all:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all-create:
	$(foreach md,$(MODULES),$(MAKE) $(md).create)

.PRECIOUS: %.create
.PHONY: $(addsuffix .create, $(MODULES))

%.create:
	if [ -a requirements.txt ]; then REQ=--file requirements.txt; fi; \
	if [[ "conda env list" =~ "$*" ]]; then cd env.$* && \
	conda create -y --name $* python=3.8 $$REQ; fi

.PRECIOUS: %.enable
.PHONY: $(addsuffix .enable, $(MODULES))

%.enable:
	conda activate $*
