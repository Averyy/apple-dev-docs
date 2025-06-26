# init(device:a:b:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a hyperbolic tangent neuron filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, a: Float, b: Float)
```

#### Return Value

A valid [`MPSCNNNeuronTanH`](mpscnnneurontanh.md) object or `nil`, if failure.

## Parameters

- `device`: The device the filter will run on.
- `a`: The “a” variable of the filter function.
- `b`: The “b” variable of the filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneurontanh/init(device:a:b:))*