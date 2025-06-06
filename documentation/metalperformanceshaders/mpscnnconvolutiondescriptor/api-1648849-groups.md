# groups

**Framework**: Metal Performance Shaders  
**Kind**: instp

The number of groups that the input and output channels are divided into.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var groups: Int { get set }
```

#### Discussion

The default value is `1`.

Groups let you reduce parametrization. If the value of this property is set to `n`, the input is divided into `n` groups with `inputFeatureChannels``/n` channels in each group. Similarly, the output is divided into `n` groups with `outputFeatureChannels/n` channels in each group.  The `ith` group in the input is only connected to the `ith` group in the output, so the number of weights (parameters) needed is reduced by a factor of `n`. Both the value of the [`inputFeatureChannels`](mpscnnconvolutiondescriptor/1648934-inputfeaturechannels.md) and [`outputFeatureChannels`](mpscnnconvolutiondescriptor/1648852-outputfeaturechannels.md) properties must be divisible by `n` and the number of channels in each group must be a multiple of `4`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648849-groups)*