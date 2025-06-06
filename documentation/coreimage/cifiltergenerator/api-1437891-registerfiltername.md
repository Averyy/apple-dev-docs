# registerFilterName(_:)

**Framework**: Core Image  
**Kind**: instm

Registers the name associated with a filter chain. 

**Availability**:
- macOS 10.5+

## Declaration

```swift
func registerFilterName(_ name: String)
```

#### Discussion

This method allows you to register the filter chain as a named filter in the Core Image filter repository. You can then create a `CIFilter` object from it using the the [`init(name:)`](cifilter/1438255-init.md) method of the [`CIFilter`](cifilter.md) class.

## Parameters

- `name`: A unique name for the filter chain you want to register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437891-registerfiltername)*