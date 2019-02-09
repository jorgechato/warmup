# Warmup
[![Build Status](https://travis-ci.org/jorgechato/warmup.svg?branch=master)](https://travis-ci.org/jorgechato/warmup)

In this repository there are 2 Algorithms exercises, 1 Design pattern and 1 Architecture design.

All the modules are in a CI/CD pipeline to run the tests. The architecture module is integrated into the deployment process with docker and heroku.

## Algorithms

### Palindrome

#### Run

```zsh
# Run palindrome
$ python -m algorithms.palindrome

# Run tests
$ python -m algorithms.palindrome_tests -v
```

### Unique triplets sum == 0

#### Run

```zsh
# Run unique triplets sum == 0
$ python -m algorithms.triplets

# Run tests
$ python -m algorithms.triplets_tests -v
```

## Design Patterns

### Object pool library

- `opool_sample` is the first iteration of the Pool.
- `opool` object pool library (Use case: database connection)
    - `opool_demo` demo of how to use the library.
    - `opool_tests` unit tests.

**Advantages**

- It offer a significant performance boost.
- It manages the connections and provides a way to reuse and share them.
- Object pool pattern is used when the rate of initializing a instance of the class is high.

#### Use

```python
from design.opool import Pool

pool = Pool([1, 2, 3])
# Lease an object from the pool
# Context manager is the way to use it.
with pool.lease() as val:
    # ...
    # use val as the object
    # ...
```

#### Run

```zsh
# Run library
$ python -m design.opool_demo

# Run tests
$ python -m design.opool_tests -v
```

## Architecture Designs

### Short URL

#### Install & Run

```zsh
# Run library
$ python -m architecture.app
```

#### Deploy

This module is automated by the CI/CD

```zsh
# Build docker
$ docker build -t short-url:latest .
$ docker run -p 8000:8000 --name short-url short-url:latest
```

You can check [the heroku deployment](https://warmup-short-url.herokuapp.com) tho.

**What is a distributed system?**

A distributed system is a network that consists of autonomous computers that are connected using a distribution middleware. They help in sharing different resources and capabilities to provide users with a single and integrated coherent network.

**What kind of difficulties commonly found when building a distributed system?**

- Security is a big challenge in a distributed environment, especially when using public networks.
- Fault tolerance could be tough when the distributed model is built based on unreliable components.
- Coordination and resource sharing can be difficult if proper protocols or policies are not in place.

**How do you solve these difficulties?**

- Enabling security layers like MFA.
- Automated Middleware Specialization approach could solve this issue.
- The ressource sharing could be solved with a reactive platform or a data streaming like Kafka.

---

## Requirements

### Must have

- [python 3.x](https://www.python.org/downloads/)
- pip3

### We recommend you

- [anaconda](https://anaconda.org/anaconda/python)

#### Install dependencies

```bash
# with anaconda
$ conda env create -f environment.yml # create virtual environment
$ conda activate warmup # enter VE
# or
$ source activate warmup
(warmup) $ conda deactivate # exit VE
```