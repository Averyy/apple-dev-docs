# write(to:atomically:)

**Framework**: Core Image  
**Kind**: method

Archives a filter generator object to a filter generator file.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func write(to aURL: URL, atomically flag: Bool) -> Bool
```

#### Return Value

Returns `true` if the object is successfully archived to the file.

#### Discussion

Use this method to save your filter chain to a file for later use.

## Parameters

- `aURL`: A  location for the file generator file.
- `flag`: Pass   to specify that Core Image should create an interim file to avoid overwriting an existing file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/write(to:atomically:))*