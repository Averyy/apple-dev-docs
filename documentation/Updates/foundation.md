# Foundation updates

**Framework**: Updates

Learn about important changes to Foundation.

#### Overview

Browse notable changes in [`Foundation`](https://developer.apple.com/documentation/Foundation).

#### June 2024

##### Predicates

- Use `Regex` regular expressions in predicates to perform pattern matching. You can use either the Swift regex domain specific language or traditional regex literals.
- Use the new `#Expression` macro when you want behavior similar to `#Predicate` but you need to return a type other than `Bool`.
- Create compound predicates by writing a `Predicate` that evaluates another `Predicate`.

##### Calendars

- Perform `Calendar` searches by calling `dates(byMatching:startingAt:in:matchingPolicy:repeatedTimePolicy:direction:)` with `DateComponent` values specifying what to search for, and receiving a `Sequence` of matching dates. You can also repeatedly add `DateComponent` values to a date with `dates(byAdding:startingAt:in:wrappingComponents:)` and receive a sequence. To add `Calendar.Component` values instead, use `dates(byAdding:value:startingAt:in:wrappingComponents:)`.

##### Format Styles

- Use the `DiscreteFormatStyle` protocol to format values that constantly change, but don’t necessarily change the formatted output on every update, such as time displays that truncate the seconds field. The following format style types conform to the new protocol: `Duration.UnitsFormatStyle`, `Duration.TimeFormatStyle`, `Date.FormatStyle`, `Date.FormatStyle.Attributed`, `Date.VerbatimFormatStyle`, `Date.VerbatimFormatStyle.Attributed`, `Date.ISO8601FormatStyle`, `Duration.UnitsFormatStyle.Attributed`, and `Duration.TimeFormatStyle.Attributed`.
- Set new configuration options on `FormatStyle` to omit specific symbols from the output and suppress grouping of large time values (for example, in order to produce `10000:00` rather than `10,000:00`).
- Use the `notation` modifier on currency format styles to specify a notation such as `compactName`, similar to how `notation` already works on numeric format styles.

##### Undo Manager

- Provide custom information for undo actions by setting user info on `UndoManager`. The info can include things like a timestamp of the action’s creation or an icon that complements the action name.
- Reveal the size of an undo manager’s current undo or redo stack with the properties `undoCount` and `redoCount`.

##### Key Value Observing

- Add a collection of shared observers to `Observable` objects that you can then add to multiple instance of the observable.
- Observables now use ARC-style weak references to their observers, preventing crashes when observers deallocate without properly removing themselves.

##### Collections

- You can initialize an `IndexSet` from a Swift `RangeSet`, and vice versa.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/foundation)*