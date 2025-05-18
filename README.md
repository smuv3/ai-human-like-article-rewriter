# AI Human-Like Article Rewriter

## About

AI Human-Like Article Rewriter is a Python-based tool that leverages OpenAI's GPT models to rewrite articles in a highly human-like, SEO-optimized, and plagiarism-free manner. Designed for content creators, bloggers, and SEO professionals, it transforms raw data or existing articles into unique, engaging markdown posts suitable for platforms like Chirpy Jekyll.

## Features

- **Human-like Rewriting:** Produces content that passes AI detection and plagiarism checks.
- **SEO Optimization:** Automatically generates SEO-friendly titles, descriptions, tags, and headings.
- **Markdown Output:** Outputs articles in Chirpy Jekyll markdown format, ready for static site generators.
- **Batch Processing:** Select and process multiple files from an input directory.
- **Customizable Settings:** Easily adjust model, temperature, max tokens, and more via `settings.ini`.
- **Promotional Content Removal:** Automatically strips out promotional or advertisement lines from input data.
- **Attribution & Compliance:** Handles attributions, copyright, disclaimers, and terms as required by the input data.
- **Interactive CLI:** User-friendly command-line interface for file selection and processing.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/OCEANOFANYTHING/ai-human-like-article-rewriter.git
   cd ai-human-like-article-rewriter
   ```

2. **Install dependencies:**

   ```sh
   pip install openai
   ```

   (You may also need `configparser` if not using Python 3.2+)

## API Key Setup

1. Obtain your OpenAI API key from [OpenAI](https://platform.openai.com/account/api-keys).
2. Open the `settings.ini` file in the project root.
3. Replace `[Place your OpenAI API key here]` with your actual API key under the `[API]` section:

   ```ini
   [API]
   OPENAI_API_KEY = sk-...
   ...
   ```

## Settings

All configuration is managed in `settings.ini`:

- **OPENAI_API_KEY:** Your OpenAI API key.
- **OPENAI_MODEL:** Model to use (e.g., `openai/gpt-4.1`).
- **OPENAI_API_BASE:** API endpoint (default: `https://models.github.ai/inference`).
- **TEMPERATURE:** Controls randomness (default: 1).
- **TOP_P:** Controls diversity (default: 1).
- **MAX_TOKENS:** Maximum output tokens (default: 20000, can be set up to 90000).
- **INPUT_DIR:** Input folder for source files (default: `data`).
- **OUTPUT_DIR:** Output folder for rewritten articles (default: `output`).

## Usage

1. Place your source articles (plain text files) in the `data` folder.
2. Run the script:

   ```sh
   python main.py
   ```

3. Select the file to process by entering its corresponding number.
4. The rewritten article will be saved in the `output` folder with the same name but `.md` extension.

## Use Cases

- **Bloggers:** Quickly rewrite and optimize articles for SEO and originality.
- **Content Agencies:** Batch process large volumes of articles for clients.
- **SEO Professionals:** Generate unique, high-quality content that passes AI and plagiarism checks.
- **Academic Writers:** Paraphrase and reformat research or reports.
- **Static Site Generators:** Produce Chirpy Jekyll-compatible markdown posts.

## Troubleshooting

- **No files found in input folder:** Ensure your source files are in the `data` directory.
- **Invalid API key:** Double-check your API key in `settings.ini`.
- **Output is empty or incomplete:** Increase `MAX_TOKENS` in `settings.ini`.
- **Encoding errors:** Ensure your input files are UTF-8 encoded.
- **Dependency errors:** Run `pip install openai` to install missing packages.

## Contributing

See [CONTRIBUTING.MD](CONTRIBUTING.MD) for guidelines on reporting issues, submitting pull requests, and code style.

## Code of Conduct

Please read our [Code of Conduct](code_of_conduct.md) to ensure a welcoming and respectful community environment.

## License

This project is licensed under the [MIT License](LICENSE).

## Changelog

See the [GitHub Releases](https://github.com/OCEANOFANYTHING/ai-human-like-article-rewriter/releases) page for a complete changelog.

## Donation & Support

If you find this project useful, consider supporting the developer:

## Contact

For questions, suggestions, or support:

- GitHub Issues: [https://github.com/OCEANOFANYTHING/ai-human-like-article-rewriter/issues](https://github.com/OCEANOFANYTHING/ai-human-like-article-rewriter/issues)
- Email: [oceanofanything@gmail.com](mailto:work.oceanofanything@gmail.com)
