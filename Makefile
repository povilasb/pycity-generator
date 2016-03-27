virtualenv_dir := pyenv
pip := $(virtualenv_dir)/bin/pip

$(virtualenv_dir): requirements/prod.txt
	virtualenv $@
	$(pip) install -r $<
