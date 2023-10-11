# Documentation: Installation and Validation of Pyomo with GLPK Solver on Amazon Linux EC2

## Introduction
This documentation outlines the steps to install the Pyomo modeling framework and the GLPK solver on an Amazon Linux EC2 instance. Additionally, it provides a sample Python code to validate the setup.

**Note**: The commands and steps mentioned in this documentation are intended for an Amazon Linux EC2 environment. Please ensure that you have the necessary permissions and understand the security implications of running these commands on your EC2 instance.

## Installation Steps

### 1. Install gcc (GNU Compiler Collection):
```shell
sudo yum install gcc
```
This command installs the GNU Compiler Collection, which is required for compiling certain packages.

### 2. Install Python3 and pip:
```shell
sudo yum -y install python3-pip
```
This command installs Python3 and pip, the Python package manager, on your EC2 instance.

### 3. Install Pyomo:
```shell
python3 -m pip install pyomo
```
This command uses pip to install the Pyomo modeling framework.

### 4. Verify Pyomo Installation:
```shell
python3 -m pip list | grep pyomo
```
This command checks if Pyomo has been successfully installed on your EC2 instance.

### 5. Download and Install GLPK Solver:

#### a. Download GLPK:
```shell
wget ftp://ftp.gnu.org/gnu/glpk/glpk-4.64.tar.gz
```
This command downloads the GLPK solver source code.

#### b. Extract GLPK:
```shell
tar -xzf glpk-4.64.tar.gz
```
Unzip and extract the GLPK source code.

#### c. Configure and Compile GLPK:
```shell
cd glpk-4.64/
./configure
make
```
These commands configure and compile the GLPK solver.

#### d. Install GLPK:
```shell
sudo make install
```
This command installs the GLPK solver on your EC2 instance.

### 6. Verify GLPK Installation:
```shell
glpsol --version
```
This command checks if the GLPK solver has been successfully installed and displays its version.

## Validation

Now that you have successfully installed Pyomo and the GLPK solver, you can validate your setup by running a sample Pyomo model. Create a Python script, for example, `pyomo_example.py`, with the following content:

```python
from pyomo.environ import *

m = ConcreteModel()
m.x = Var(within=NonNegativeReals)
m.obj = Objective(expr=m.x)
m.con = Constraint(expr=m.x >= 1)

s = SolverFactory('glpk')
s.solve(m)

m.display()
```

To run the script:

1. Open a terminal on your EC2 instance.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

```shell
python3 pyomo_example.py
```

If everything is set up correctly, this script will create a simple Pyomo model, solve it using the GLPK solver, and display the results on the terminal.

## Conclusion

This documentation provides a step-by-step guide for installing Pyomo and the GLPK solver on an Amazon Linux EC2 instance. It also includes a sample Python script to validate the installation. With this setup, you can now utilize Pyomo and the GLPK solver for mathematical modeling and optimization tasks on your EC2 instance.