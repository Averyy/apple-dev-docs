# Atomic Operations

**Framework**: Kernel

Increment and decrement numbers, perform compare-and-swap operations, and manipulate other data atomically. 

## Topics

### Test Operations
- [OSTestAndClear](1576463-ostestandclear.md)
  Bit test and clear operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSTestAndSet](1576456-ostestandset.md)
  Bit test and set operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
### Increment
- [OSIncrementAtomic](1576460-osincrementatomic.md)
  32-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSIncrementAtomic8](1576477-osincrementatomic8.md)
  8-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSIncrementAtomic16](1576484-osincrementatomic16.md)
  16-bit increment operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSIncrementAtomic64](1576480-osincrementatomic64.md)
  64-bit increment.
### Decrement
- [OSDecrementAtomic](1576455-osdecrementatomic.md)
  32-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSDecrementAtomic8](1576458-osdecrementatomic8.md)
  8-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSDecrementAtomic16](1576468-osdecrementatomic16.md)
  16-bit decrement operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSDecrementAtomic64](1576449-osdecrementatomic64.md)
  64-bit decrement.
### Compare and Swap
- [OSCompareAndSwap](1576450-oscompareandswap.md)
  Compare and swap operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSCompareAndSwap64](1576485-oscompareandswap64.md)
  64-bit compare and swap operation.
- [OSCompareAndSwapPtr](1576461-oscompareandswapptr.md)
  Compare and swap operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
### Additions
- [OSAddAtomic](1576452-osaddatomic.md)
  32-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSAddAtomic8](1576483-osaddatomic8.md)
  8-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSAddAtomic16](1576475-osaddatomic16.md)
  16-bit add operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSAddAtomic64](1576451-osaddatomic64.md)
  64-bit atomic add operation.
### Boolean Operations
- [OSBitAndAtomic](1576481-osbitandatomic.md)
  32-bit logical and operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitAndAtomic8](1576487-osbitandatomic8.md)
  8-bit logical and operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitAndAtomic16](1576453-osbitandatomic16.md)
  16-bit logical and operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitOrAtomic](1576467-osbitoratomic.md)
  32-bit logical or operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitOrAtomic8](1576478-osbitoratomic8.md)
  8-bit logical or operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitOrAtomic16](1576466-osbitoratomic16.md)
  16-bit logical or operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitXorAtomic](1576476-osbitxoratomic.md)
  32-bit logical xor operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitXorAtomic8](1576459-osbitxoratomic8.md)
  8-bit logical xor operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.
- [OSBitXorAtomic16](1576464-osbitxoratomic16.md)
  16-bit logical xor operation, performed atomically with respect to all devices that participate in the coherency architecture of the platform.

## See Also

- [Data Types](libkern/data_types.md)
  Create strings, numbers, collections, data objects, and the other standard types employed by drivers and kernel extensions.
- [Byte Order Utilities](libkern/byte_order_utilities.md)
  Convert values between big-endian and little-endian formats. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/libkern/atomic_operations)*