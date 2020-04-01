# TrueCase


![Main](https://github.com/daltonfury42/truecase/workflows/Main/badge.svg) ![Publish PyPI](https://github.com/daltonfury42/truecase/workflows/Publish%20Python%20distributions%20to%20PyPI/badge.svg)

A language independent, statistical, language modeling
based tool in Python that restores case information for text.

The model was inspired by the paper of [Lucian Vlad Lita  et al., tRuEcasIng](https://www.cs.cmu.edu/~llita/papers/lita.truecasing-acl2003.pdf) but with some simplifications.


A model trained on NLTK English corpus comes with the package by default, 
and for other languages, a script is provided to create the model. This model is 
not perfect, train the system on a large and recent dataset to achieve 
the best results (e.g. on a recent dump of Wikipedia).

### Prerequisites

- Python 3

The project uses NLTK. Find install instructions [here](https://www.nltk.org/install.html).

### Installing

```bash
pip install truecase
```

## Usage

Simple usecase:

```python
>>> import truecase
>>> truecase.get_true_case('hey, what is the weather in new york?')
'Hey, what is the weather in New York?''
```

## Training your own model

TODO. For now refer to Trainer.py

## Contributing

I see a lot of space for improvement. Feel free to fork and improve. Do sent a pull request.

## Authors

* **Dalton Fury** - *Initial work* - [daltonfury42](https://github.com/daltonfury42)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

## Acknowledgments

* [Lucian Vlad Lita  et al., tRuEcasIng](https://www.cs.cmu.edu/~llita/papers/lita.truecasing-acl2003.pdf)
* Borrowed a lot of code, and the idea from [truecaser](https://github.com/nreimers/truecaser/blob/master/README.md) by [nreimers](https://github.com/nreimers)
