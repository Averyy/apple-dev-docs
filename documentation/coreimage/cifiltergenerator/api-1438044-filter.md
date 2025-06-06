# filter()

**Framework**: Core Image  
**Kind**: instm

Creates a filter object based on the filter chain.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func filter() -> CIFilter
```

#### Return_value

A `CIFilter` object.

#### Discussion

The topology of the filter chain is immutable, meaning that any changes you make to the filter chain are not reflected in the filter. The returned filter holds the export input and output keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438044-filter)*