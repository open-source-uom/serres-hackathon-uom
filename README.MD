

# Open Source UoM Serres Hackathon 2023

Hackathon repo: https://github.com/serrestech/hackathon-topic

The Tile Factory 1981 Problem Solver is a Python program that solves the Tile Factory 1981 Problem. This problem is a classic optimization problem that involves finding the optimal way to produce tiles of different sizes using a limited set of machines.

## Table of Contents

- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [Contributing](#contributing)
- [License](#license)

## Background

Suppose you work for a large factory making decorative ceramic wall tiles back in 1981!

You are member of the R&D team and you supervisors ask your team to find a way help the factory solve several problems.

The most urgent problem comes from an old cutting machine which produces many tile scraps with a "strange shape".

Your team have to find an innovative way to sell these strange tiles so the company doesn't have to throw them away or recycle them back.

Your team has only 42 hours to solve all the tasks is asked for! If you solve all the tasks you get 350pts and win a salary increase!

## Installation

To install the Tile Factory 1981 Problem Solver, simply clone the repository and install the required dependencies:

```
git clone [https://github.com/your-username/tile-factory-1981.git](https://github.com/Open-Source-UoM/serres-hackathon-uom)
cd serres-hackathon-uom
npm install
npm run dev
```

## Usage

To use the Tile Factory 1981 Problem Solver,
simply use the Graphical User Interface(GUI) that will lunch on local host with the previous commands.

```

## Algorithm

The Tile Factory 1981 Problem Solver uses a dynamic programming algorithm to solve the problem. The algorithm works as follows:

- Define a state as a tuple (i, j, k), where i is the order number, j is the number of tiles produced so far, and k is a binary mask representing the machines used so far.
- Define a function f(i, j, k) as the minimum number of machine hours needed to produce the i-th order, given that j tiles of the required sizes have already been produced, and the machines represented by the binary mask k have been used so far.
- The base case is f(0, 0, 0) = 0.
- For each state (i, j, k), compute f(i, j, k) as follows:
  - If j >= the number of tiles required for the i-th order, then f(i, j, k) = f(i+1, 0, k).
  - Otherwise, for each unused machine m that can produce a tile of the required size, compute f(i, j+machines[m], k|2^m) + (j+machines[m])*(cost of machine m).
  - Take the minimum over all possible choices of m.
- The answer is f(1, 0, 0).

## Contributing

