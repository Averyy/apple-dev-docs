# SiriScenarioSubject.ScenarioReport

**Framework**: Siri Evaluations  
**Kind**: struct  
**Role**: Structure

What the Xcode report shows for one scenario: Diagnostics, Scenario (if it has any expectations of its own), then each turn.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
struct ScenarioReport
```

## Overview

Opaque: made by the evaluation and read only by the report. A type of its own because Xcode titles the report page with the value’s type name; its contents are text for display, not a format to parse. It encodes as nested sections of text rows (see SiriReport.swift). The scenario builds one too, holding only what it expects (`SiriScenario.expected`), which Xcode compares with this one row by row.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirievaluations/siriscenariosubject/scenarioreport)*