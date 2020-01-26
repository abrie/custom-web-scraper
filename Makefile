START=$(shell jq .start secrets/secrets.json)
STEP1_OUTPUT="process/step1.txt"
STEP2_OUTPUT="process/step2.txt"
STEP3_OUTPUT="process/step3"
STEP4_OUTPUT="process/step4"

.PHONEY: step1
step1:
	START=$(START) OUTPUT=$(STEP1_OUTPUT) ./step1.sh

.PHONEY: step2
step2:
	# Note use of doubled $$ signs, necessary when awk is used in a Makefile
	awk '{print $$1,$$3}' $(STEP1_OUTPUT) > $(STEP2_OUTPUT)

.PHONEY: step3
step3:
	python3 step3.py $(STEP2_OUTPUT) $(STEP3_OUTPUT)

.PHONEY: step4
step4:
	python3 step4.py $(STEP3_OUTPUT) $(STEP4_OUTPUT)

