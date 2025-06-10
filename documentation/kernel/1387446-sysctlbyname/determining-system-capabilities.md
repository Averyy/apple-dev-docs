# Determining system capabilities

**Framework**: Kernel

Interrogate the system for processor, cache, and topology information.

#### Overview

Obtain information about parameters related to processor availability, cache size, and performance-level characteristics on the system by using the [`sysctlbyname`](1387446-sysctlbyname.md) function. These parameters provide details about your system that can aid in tuning performance. For example, you can obtain the count of the highest-performing processor cores to spawn a worker thread for each core. Or you can determine the size of the L2 cache and the number of processor cores that share it to perform software cache-blocking optimization.

##### 3901384

The system enables a processor core when it’s powered on and available for thread scheduling. Each logical processor core executes a software thread that the operating system manages. On systems where the number of logical processor cores exceeds the number of physical processor cores, two or more logical processor cores share a physical core through simultaneous multithreading (SMT). The following parameters provide processor availability information about the system on chip (SoC):

##### 3901385

The following parameters provide processor core performance-level information. First, determine the number of types of processor cores with `hw.nperflevels`. Then, for each of the parameters, replace  with a number between `0` and the number of performance levels minus one. Lower values of  indicate higher-performance core types.

Querying the following parameters is equivalent to querying the per-performance-level information for the least performant core. For example, `hw.l1dcachesize` is equivalent to `hw.perflevel[``].l1dcachesize`, where  is `hw.nperflevels` minus one.

##### 3901382

The following parameters provide cache line, memory, and page size information:

## See Also

- [Determining Instruction Set Characteristics](1387446-sysctlbyname/determining_instruction_set_characteristics.md)
  Interrogate the system for details about the instruction set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1387446-sysctlbyname/determining_system_capabilities)*