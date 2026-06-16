from education.pipeline.orchestrator import EducationalPipeline

if __name__ == "__main__":
    pipeline = EducationalPipeline()
    output_path = pipeline.generate_presentation("Artificial Intelligence")
    print(f"Presentation generated successfully: {output_path}")
