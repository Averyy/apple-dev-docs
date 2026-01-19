---
source: coremltools
framework: coremltools
url: https://apple.github.io/coremltools/docs-guides/source/installing-coremltools.html
---

# Installing Core ML Tools

**

- [.md](../_sources/source/installing-coremltools.md)
- **

.pdf

**

# Installing Core ML Tools

 Table of contents 

## Contents

# Installing Core ML Tools

This page describes how to install the [coremltools](https://github.com/apple/coremltools) Python package on macOS (10.13+) and Linux.

Supported Python and MacOS Versions

The current version of coremltools ([version 8.0](https://github.com/apple/coremltools)) includes wheels for Python 3.7, 3.8, 3.9, 3.10, 3.11, and 3.12. The last stable release of coremltools to support Python 2 is version 4.0.

The supported MacOS versions are as follows:

- Core ML Tools 4.1 supports macOS 10.13 and newer.
- Core ML Tools 5, 6, and 7 support macOS 10.15 and newer.

## Prerequisites

For Beginners

If you are using macOS, you should already be familiar with the [Mac Terminal app command line](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/CommandLInePrimer/CommandLine.html#//apple_ref/doc/uid/TP40004268-CH271-BBCBEAJD) to perform tasks such as installations and updates. If you are using Linux, you should already be familiar with [basic Shell commands in Linux](https://www.geeksforgeeks.org/basic-shell-commands-in-linux/).

Before installing coremltools, you need [Python](https://www.python.org/downloads/) and the [pip](https://pip.pypa.io/en/stable/) installer.

The `coremltools` package supports [Python 3](https://www.python.org/download/releases/3.0/). We recommend that you install Python 3.6 or newer. Use a Python package manager such as [Conda](https://docs.conda.io/en/latest/index.md) or [venv](https://docs.python.org/3/library/venv.md) to install the newest version of Python and other dependencies. [Conda](https://docs.conda.io/en/latest/index.md) is recommended because it is the most reliable way to install all required dependencies.

## Install or Build Core ML Tools

To install Core ML Tools, use one of the following methods:

- The Conda package installer: Python is installed automatically. You can install [pip](https://pip.pypa.io/en/stable/) after setting up the Conda environment. Skip to [Set Up Conda](#set-up-conda).
- A virtual environment: Install [pip](https://pip.pypa.io/en/stable/), and then use [venv](https://docs.python.org/3/library/venv.md), which also installs Python. Skip to [Set Up a New Virtual Environment](#set-up-a-new-virtual-environment).
- Install a Python wheel: To download and install the most recent (or any available) Python wheel (`.whl` file) for Core ML Tools, see [Install From Source](#install-from-source).
- Build from source: To build the most recent (or any available) version of Core ML Tools, see [Build From Source](#build-from-source).

To install third-party frameworks, libraries, or other software, see [Install Third-party Packages](#install-third-party-packages).

## Set Up Conda

Follow these steps:

1. Use the appropriate [Miniconda installer](https://docs.conda.io/en/latest/miniconda.md) for your operating system.
2. Create a Conda environment for `coremltools` using the following command:

```
conda create --name coremltools-env
```

1. Activate your virtual environment using the following command:

```
conda activate coremltools-env
```

1. Install `pip` for this environment using the following command:

```
conda install pip
```

1. Follow the instructions in [Install Core ML Tools](#install-core-ml-tools).

## Set Up a New Virtual Environment

Follow these steps:

1. Install `pip` using the following command:

```
python -m pip install --user --upgrade pip
```

1. Create a virtual environment using the following command:

```
python -m venv coremltools-venv
```

1. Activate the virtual environment:

```
source coremltools-venv/bin/activate
```

1. Follow the instructions in [Install Core ML Tools](#install-core-ml-tools).

## Install Core ML Tools

Use the following command to install or upgrade to [version 7.1](https://github.com/apple/coremltools) of Core ML Tools:

```
pip install -U coremltools
```

## Install Third-party Packages

Install the third-party source packages for your conversions (such as [TensorFlow](https://www.tensorflow.org) and [PyTorch](https://pytorch.org)) using the package guides provided for them. The `coremltools` package does *not* include the third-party source packages.

## Install From Source

The continuous integration (CI) system linked to the `coremltools` repo builds a [Python wheel](https://pypi.org/project/wheel/) from the master branch whenever a commit is merged. To get the latest updates to the code base, you can get this wheel from the CI job and install it.

To access the wheel for a particular `coremltools` release, follow these steps:

1. Go to the [coremltoolsrepository](https://github.com/apple/coremltools) on GitHub, scroll down to the **README.md** heading, and click the **build passing** button. The **Branches** tab appears:
2. Click the **passed** button to show the **Pipeline** tab:
3. Click a wheel in the **Build** column. For example, in the previous figure, the **build_wheel_macos_py38** wheel is highlighted for clicking. After clicking a wheel, the raw job log appears, with the **Download** and **Browse** buttons in the right column:
4. Click the **Download** button to download the `dist` folder with the wheel files.
5. Install a wheel file using `pip`. For example, use the following command to install the `coremltools-4.0-cp38-none-macosx_10_12_intel.whl` wheel file for the 4.0 version of Core ML Tools:

```
pip install coremltools-4.0-cp38-none-macosx_10_12_intel.whl
```

## Build From Source

To build Core ML Tools and its dependent libraries from source, you need to install [CMake](https://cmake.org/) to configure the project.

To perform the build, fork and clone the [coremltoolsrepository](https://github.com/apple/coremltools) and run the [build.sh](https://github.com/apple/coremltools/blob/master/scripts/build.sh) script:

```
zsh -i scripts/build.sh
```

The script creates a new `build` folder with the coremltools distribution, and a `dist` folder with Python wheel files.

For more information about building Core ML Tools, see [Building From Source](https://github.com/apple/coremltools/blob/master/BUILDING.md).

## Upgrade Core ML Tools

For either Conda or virtual environments, see [Install Core ML Tools](#install-core-ml-tools) for the command to upgrade Core ML Tools.

** Contents
