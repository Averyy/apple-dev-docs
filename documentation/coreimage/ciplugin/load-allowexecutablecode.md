# load(_:allowExecutableCode:)

**Framework**: Core Image  
**Kind**: method

Loads filters from an image unit that have the appropriate executable status.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class func load(_ url: URL!, allowExecutableCode: Bool)
```

#### Discussion

You need to call this method only once to load a specific image unit. The behavior of this method is not defined for multiple calls for the same image unit. If you pass [`false`](https://developer.apple.com/documentation/swift/false) for the `allowExecutableCode` parameter, Core Image will load only pure kernel filters that run entirely on the GPU, ignoring filters implemented using compiled Objective-C code.

## Parameters

- `url`: The location of the image unit to load.
- `allowExecutableCode`:   to load all filters from the image unit, or   to load only those filters without CPU executable code.

## See Also

- [class func loadAllPlugIns()](ciplugin/loadallplugins.md)
  Scans directories for files that have the `.plugin` extension and then loads the image units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/load(_:allowexecutablecode:))*