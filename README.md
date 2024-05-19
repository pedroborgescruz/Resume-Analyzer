# Resume Analyzer

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Recruiters, especially those at big tech companies, often need to sift through thousands of resumes to identify suitable candidates. Consequently, developing tools to assist in this process is a natural progression. **Resume Analyzer** is a tool leveraging NLP-related libraries in Python - such as Gensim, NLTK, spaCy, and RegEx - and data manipulation to create tools designed to support your hiring process.

### Dataset:
A collection of 2400+ Resume Examples taken from livecareer.com for categorizing a given resume into any of the labels defined in the dataset: [Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset).

## Features

- Analyze resumes to extract key information.
- Provide insights and summaries of resumes.
- Customizable to suit your specific needs.
- Easy-to-use interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/pedroborgescruz/resume-analyzer.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Navigate to the project directory:

    ```bash
    cd resume-analyzer
    ```

2. Run the application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

4. Paste your resume in the provided textarea and click on "Go" to analyze it.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
