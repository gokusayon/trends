include commons.mk

SERVICE_NAME = dashboard
SERVICE_LANG = ts

.PHONY: all build run

build:
	${NPM_DR_LINUX} "${NPM_BUILD_CMD}"

run:
	${NPM_RUN_LINUX} "${NPM_PKG_STAGE_CMD}"

update:
	${NPM_UPDATE_ANGULAR} "${UPDATE_ANGULAR}"

# Target pattern to match any from parent
%: ;