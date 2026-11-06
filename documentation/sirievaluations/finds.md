# Finds

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

An expectation that Siri surfaces specific app entities by search or resolution.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct Finds
```

## Overview

Use `Finds` to name the app entities Siri finds when it searches or resolves entities in your app for a request. The expectation holds when Siri finds an entity that matches, including its type. A bare entity definition matches any entity of that type, and you can add constraints on its properties with [`expect`](../AppIntentsTesting/appentitydefinition/expect.md).

`Finds` checks entities Siri finds by searching. To check entities that are visible onscreen, use [`OnScreen`](./onscreen.md). The two are separate because the entities reach Siri by different paths. One doesn’t stand in for the other. A found entity doesn’t always carry the details Siri tells the person. Use [`SiriResponse`](./siriresponse.md) for facts that only the reply contains.

## Topics

### Creating a find expectation
- [init(() -> [any AppEntityExpectationProviding])](./finds/init%28_%29.md)
  Creates an expectation that Siri surfaces each entity in the block by search or resolution.
- [enum EntityFindExpectationBuilder](./entityfindexpectationbuilder.md)
  A result builder that collects the entities a finds expectation requires.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Expectations
- [struct Calls](./calls.md)
  An expectation that Siri calls, or doesn’t call, a set of intents during a turn or scenario.
- [struct Loads](./loads.md)
  An expectation that Siri loads specific app skills.
- [struct OnScreen](./onscreen.md)
  An expectation that specific app entities are onscreen.
- [struct SiriResponse](./siriresponse.md)
  An expectation that the reply Siri gives contains specific text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/finds)*