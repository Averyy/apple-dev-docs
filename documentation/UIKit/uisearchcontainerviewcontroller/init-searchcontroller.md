# init(searchController:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns a search container view controller with the specified search controller object.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(searchController: UISearchController)
```

#### Return Value

An initialized search container view controller.

#### Discussion

After initializing the search container view controller, embed it in your container view controller normally.

## Parameters

- `searchController`: The search controller managing the search results. This parameter must not be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchcontainerviewcontroller/init(searchcontroller:))*