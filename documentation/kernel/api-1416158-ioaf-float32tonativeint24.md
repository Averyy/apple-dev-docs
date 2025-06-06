# IOAF_Float32ToNativeInt24

**Framework**: Kernel  
**Kind**: func

Converts 32-bit floating point to native 24-bit integer

**Availability**:
- macOS 10.7+

## Declaration

```swift
void IOAF_Float32ToNativeInt24(const Float32 *src, UInt8 *dest, unsigned int count);
```

## Parameters

- `src`: Pointer to the data to convert
- `dest`: Pointer to the converted data
- `count`: The number of items to convert

## See Also

- [IOAF_Float32ToInt8](3242800-ioaf_float32toint8.md)
- [IOAF_Float32ToNativeInt16](1416160-ioaf_float32tonativeint16.md)
  Converts 32-bit floating point to native 16-bit integer
- [IOAF_Float32ToNativeInt32](1416171-ioaf_float32tonativeint32.md)
  Converts 32-bit floating point to native 32-bit integer
- [IOAF_Float32ToSwapInt16](1416149-ioaf_float32toswapint16.md)
  Converts 32-bit floating point to non-native 16-bit integer
- [IOAF_Float32ToSwapInt24](1416187-ioaf_float32toswapint24.md)
  Converts 32-bit floating point to non-native 24-bit integer
- [IOAF_Float32ToSwapInt32](1416170-ioaf_float32toswapint32.md)
  Converts 32-bit floating point to non-native 32-bit integer
- [IOAF_Int8ToFloat32](3242801-ioaf_int8tofloat32.md)
- [IOAF_NativeInt16ToFloat32](1416175-ioaf_nativeint16tofloat32.md)
  Converts native 16-bit integer float to 32-bit float
- [IOAF_NativeInt24ToFloat32](1416169-ioaf_nativeint24tofloat32.md)
  Converts native 24-bit integer float to 32-bit float
- [IOAF_NativeInt32ToFloat32](1416152-ioaf_nativeint32tofloat32.md)
  Converts native 32-bit integer float to 32-bit float
- [IOAF_SwapInt16ToFloat32](1416179-ioaf_swapint16tofloat32.md)
  Converts non-native 16-bit integer float to 32-bit float
- [IOAF_SwapInt24ToFloat32](1416164-ioaf_swapint24tofloat32.md)
  Converts non-native 24-bit integer float to 32-bit float
- [IOAF_SwapInt32ToFloat32](1416183-ioaf_swapint32tofloat32.md)
  Converts non-native 32-bit integer float to 32-bit float


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1416158-ioaf_float32tonativeint24)*