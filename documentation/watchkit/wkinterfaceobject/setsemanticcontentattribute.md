# setSemanticContentAttribute(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the semantic description of the object’s contents, used to determine whether its content should be flipped when switching between left-to-right and right-to-left layouts.

**Availability**:
- watchOS 2.1+

## Declaration

```swift
func setSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute)
```

## Overview

Some objects should not flip when switching between left-to-right and right-to-left layouts. Typically, this occurs because the object is part of the playback controls or represents physical directions (up, down, left, right) that don’t change. Instead of thinking about whether or not an object should change its orientation, select the semantic content attribute that best describes the object.

For example, set the semantic content attribute on a [`WKInterfaceGroup`](https://developer.apple.com/documentation/watchkit/wkinterfacegroup) object to control whether the group should flip the horizontal ordering of its contents when moving between left-to-right and right-to-left languages.

## Parameters

- `semanticContentAttribute`: The object’s semantic content attribute. For a list of possible values, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setsemanticcontentattribute(_:))*