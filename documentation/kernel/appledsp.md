# AppleDSP

**Framework**: Kernel  
**Role**: API Collection

Perform digital signal processing on data.

## Topics

### Biquadratic Infinite Impulse Response (IIR) Filters
- [vDSP_biquad2](./api-1532195-vdsp_biquad2.md)
  Applies a single-precision stereo biquadratic IIR filter.
- [vDSP_biquad2_CreateSetup](./api-1532224-vdsp_biquad2_createsetup.md)
  Builds a data structure that contains precalculated single-precision data for stereo biquadratic filter functions to use.
- [IIRChannel](./iirchannel.md)
  Constants that specify which channels a stereo biquadratic filter operates.
- [vDSP_biquad2_CopyState](./api-1532220-vdsp_biquad2_copystate.md)
  Copies the filter state from one biquadratic filter object to another.
- [vDSP_biquad2_ResetState](./api-1532215-vdsp_biquad2_resetstate.md)
  Resets the filter state of a single-precision stereo biquadratic filter object.
- [vDSP_biquad2_DestroySetup](./api-1532201-vdsp_biquad2_destroysetup.md)
  Destroys a single-precision stereo biquadratic IIR setup object.
### Recursive Filters
- [vDSP_deq22](./api-1532225-vdsp_deq22.md)
  Performs two-pole, two-zero recursive filtering on a single-precision vector.
### Conversion Functions
- [vDSP_vsmfix24](./api-1532200-vdsp_vsmfix24.md)
  Scales and converts single-precision floating-point values to signed 24-bit integer values.
- [vDSP_vsmfixu24](./api-1532178-vdsp_vsmfixu24.md)
  Scales and converts single-precision floating-point values to unsigned 24-bit integer values.
- [vDSP_vfix16](./api-1532172-vdsp_vfix16.md)
  Converts an array of single-precision floating-point values to signed 16-bit integer values, rounding toward zero.
- [vDSP_vfix32](./api-1532198-vdsp_vfix32.md)
  Converts an array of single-precision floating-point values to signed 32-bit integer values, rounding toward zero.
- [vDSP_vflt16](./api-1532204-vdsp_vflt16.md)
  Converts an array of signed 16-bit integers to single-precision floating-point values.
- [vDSP_vflt24](./api-1532208-vdsp_vflt24.md)
  Converts signed 24-bit integer values to single-precision floating-point values.
- [vDSP_vflt32](./api-1532181-vdsp_vflt32.md)
  Converts an array of signed 32-bit integers to single-precision floating-point values.
- [vDSP_vfltu24](./api-1532185-vdsp_vfltu24.md)
  Converts unsigned 24-bit integer values to single-precision floating-point values.
### Convolution and Correlation Functions
- [vDSP_conv](./api-1532184-vdsp_conv.md)
  Performs either correlation or convolution on two real single-precision vectors.
### Vector Absolute Functions
- [vDSP_vabs](./api-1532216-vdsp_vabs.md)
  Calculates the absolute value of each element in the supplied single-precision vector using the specified stride.
### Vector Arithmetic Functions
- [vDSP_vadd](./api-1532191-vdsp_vadd.md)
  Adds two single-precision vectors.
- [vDSP_vma](./api-1532193-vdsp_vma.md)
  Adds a single-precision vector to the product of two single-precision vectors.
- [vDSP_vsub](./api-1532189-vdsp_vsub.md)
  Subtracts two single-precision vectors.
- [vDSP_vmul](./api-1532206-vdsp_vmul.md)
  Multiplies two single-precision vectors.
- [vDSP_vsmul](./api-1532223-vdsp_vsmul.md)
  Multiplies a single-precision scalar value by a single-precision vector.
- [vDSP_vdiv](./api-1532168-vdsp_vdiv.md)
  Divides two single-precision vectors.
### Vector Extrema Functions
- [vDSP_maxmgv](./api-1532187-vdsp_maxmgv.md)
  Calculates the maximum magnitude in a single-precision vector.
### Vector Reduction Functions
- [vDSP_rmsqv](./api-1532207-vdsp_rmsqv.md)
  Calculates the root mean square of a single-precision vector.
- [vDSP_svesq](./api-1532179-vdsp_svesq.md)
  Calculates the sum of values and the sum of squares in a single-precision vector.
- [vDSP_svs](./api-1532174-vdsp_svs.md)
  Calculates the sum of signed squares in a single-precision vector.

## See Also

### Utilities
- [Debugging](./debugging.md)
  Debug your kernel extensions using the kernel debugger, assertions, exceptions, backtraces, and logging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/appledsp)*