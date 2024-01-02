all_test:
	python -m unittest discover tests

ifdef file
    test:
		python -m unittest tests/$(file)
else
    test:
		@echo "Error: file argument not provided. Use file=<test_file>"
		exit 1
endif

.PHONY: test