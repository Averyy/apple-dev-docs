# playgroundSharedDataDirectory

**Framework**: Playground Support  
**Kind**: data

The path to the directory containing data shared between all playgrounds in Xcode.

**Availability**:
- macOS 11.0+
- Xcode 12.0+

## Declaration

```swift
let playgroundSharedDataDirectory: URL
```

#### Discussion

Use this directory to store data that must be persisted between playground runs or shared between multiple playgrounds.

## See Also

- [class PlaygroundKeyValueStore](playgroundkeyvaluestore.md)
  A data storage container you use to persist information across different sessions.
- [enum PlaygroundValue](playgroundvalue.md)
  The types you can save in the key-value store or send in messages to live views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundshareddatadirectory)*