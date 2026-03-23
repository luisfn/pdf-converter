IMAGE_NAME = html2pdf

build:
	docker build -t $(IMAGE_NAME) .

convert:
	@if [ -z "$(INPUT)" ]; then \
		echo "Usage: make convert INPUT=path/to/file.html [OUTPUT=path/to/output.pdf]"; \
		exit 1; \
	fi
	@INPUT_RAW=$$(eval echo "$(INPUT)"); \
	INPUT_ABS=$$(realpath "$$INPUT_RAW"); \
	INPUT_DIR=$$(dirname "$$INPUT_ABS"); \
	INPUT_FILE=$$(basename "$$INPUT_ABS"); \
	if [ -n "$(OUTPUT)" ]; then \
		OUTPUT_RAW=$$(eval echo "$(OUTPUT)"); \
		mkdir -p "$$(dirname "$$OUTPUT_RAW")"; \
		OUTPUT_ABS=$$(cd "$$(dirname "$$OUTPUT_RAW")" && pwd)/$$(basename "$$OUTPUT_RAW"); \
		OUTPUT_DIR=$$(dirname "$$OUTPUT_ABS"); \
		OUTPUT_FILE=$$(basename "$$OUTPUT_ABS"); \
		docker run --rm \
			-v "$$INPUT_DIR:/input" \
			-v "$$OUTPUT_DIR:/output" \
			$(IMAGE_NAME) /input/$$INPUT_FILE -o /output/$$OUTPUT_FILE; \
	else \
		docker run --rm \
			-v "$$INPUT_DIR:/input" \
			$(IMAGE_NAME) /input/$$INPUT_FILE; \
	fi

.PHONY: build convert
