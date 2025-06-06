# adjustTextPosition(byCharacterOffset:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Moves the insertion point forward or backward in the current text input object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func adjustTextPosition(byCharacterOffset offset: Int)
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

## Parameters

- `offset`: The number of characters to adjust the insertion point by. A positive value moves the insertion point forward (according to the text storage direction for the current language). A negative value moves the insertion point backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdocumentproxy/adjusttextposition(bycharacteroffset:))*