# init(_:)

**Framework**: Siri Evaluations  
**Kind**: init  
**Role**: Initializer

Creates an expectation that Siri surfaces each entity in the block by search or resolution.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
init(@EntityFindExpectationBuilder _ content: () -> [any AppEntityExpectationProviding])
```

## Discussion

A found entity carries what Siri had for it when it found it. Siri usually finds an entity your app indexes in your app’s Spotlight index, as a reference: it then carries each property your scenario’s `Finds` expectations check on its type, as your app indexed it, or, where your index can’t give it (below), as your app returns it for the entity’s identifier, both read when Siri found it. An intent of your app that Siri starts before a read finishes drops what was read after it started: the entity keeps what your index held before, and a check on the rest fails, the report saying it’s unable to be graded: match such an entity with `expectIdentifier(_:)`. An intent of another app that changes data your app shares, through EventKit or an app group, isn’t detected. When Siri’s search read only a few of its properties from your index, the entity keeps those and is read for the other checked ones like a reference. On a reference, or an entity that carries only those few properties, a check on a property it doesn’t carry fails, `.isNil` included, and the report says the property wasn’t read; one your app indexed or returned with no value has none, so `.isNil` holds on it, except a `@DeferredProperty` your app returned no value for, which reads as not read, since one whose getter threw comes back the same. When Siri gets the entity from your app’s own query instead, it carries what that query returned, and a property it doesn’t carry has no value, so `.isNil` holds on it. A property of the entity itself whose name begins with `_`, or that is named `liveAppEntityFeedId`, is never relayed: `.isNil` holds on it when Siri’s search returned the entity whole, and a check on it fails as not read otherwise, a partial’s included. A check on `id` is unable to be graded, since App Intents doesn’t list an entity’s `id` as a property: match an instance with `expectIdentifier(_:)`.

A scenario that checks a property of your app’s entities, here or in `.result(…)`, launches your app in the background as its run starts, before Siri’s first turn, so Siri meets your app running; one that checks none leaves your app as it was.

An entity your app doesn’t index can be found through your `EntityStringQuery`, which receives Siri’s search phrase, so match a title within a longer phrase.

A property you check reads from your Spotlight index, without asking your app, when you index it with a key: `@Property(indexingKey:)`, `@Property(customIndexingKey:)` or `@ComputedProperty(indexingKey:)`. An entity that adopts a schema indexes the properties its schema gives keys to; give a custom key to any other. A string, number, Boolean, date or URL reads back; so do a list under a list attribute, such as `keywords`, and an enum under a string attribute, both checked with `.matches(_:)`. Where your index holds nothing for a property, an optional single value has no value, so `.isNil` holds on it; Spotlight stores no empty list, so a list that can’t be nil is empty; anything else, an optional list or a single value that can’t be nil, is read from your app. A place, a value set only in your own `attributeSet`, text content, people and recurrence rules don’t read back from the index whole, so they’re read from your app. A property your app returns holding a list of more than 100 items, at any depth, reads as not read.

The following shows how you can use the builder syntax:

```swift
Finds {
    EventEntity.expect(title: .equals("The expected title"))
}
```

## See Also

### Creating a find expectation
- [enum EntityFindExpectationBuilder](../entityfindexpectationbuilder.md)
  A result builder that collects the entities a finds expectation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/finds/init(_:))*