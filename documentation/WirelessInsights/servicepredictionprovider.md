# ServicePredictionProvider

**Framework**: WirelessInsights  
**Kind**: class

A class that provices cellular service predictions about upcoming events and anomalies.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
final class ServicePredictionProvider
```

#### Overview

To receive predictions about changing cellular conditions, start by initializing and retaining an instance of this class. Next, iterate over the [`servicePredictions`](servicepredictionprovider/servicepredictions.md) asynchronous sequence with a `for`-`await`-`in` loop.

Each time your loop receives updated [`ServicePrediction`](serviceprediction.md) instances, you can inspect their [`predictedStartTime`](serviceprediction/predictedstarttime.md), [`predictedInterval`](serviceprediction/predictedinterval.md), and [`impact`](serviceprediction/impact-swift.property.md) properties to determine if your app needs to take action in advance of a potentially disruptive event.

While processing predictions from the [`servicePredictions`](servicepredictionprovider/servicepredictions.md) sequence, gracefully handle any errors that it throws. The [`ServicePredictionError.unsupportedDevice`](servicepredictionerror/unsupporteddevice.md) error indicates that WirelessInsights won’t provide any predictions on this device. However, other errors indicate recoverable failures, such as [`ServicePredictionError.connectionError`](servicepredictionerror/connectionerror.md).

The following example shows a class that creates a [`Task`](https://developer.apple.com/documentation/Swift/Task) to receive service predictions and call a private helper method when it receives a sufficiently important prediction.

```swift
class PredictionHandler {

   private let servicePredictionProvider = ServicePredictionProvider()
   private let predictionHandlerTask: Task<Void, Never>

   init() {
       predictionHandlerTask = Task {
           do {
               for try await predictions in servicePredictionProvider.servicePredictions {
                   // Take action if any prediction in the current set
                   // has a sufficiently high impact and duration,
                   // with medium or higher confidence.
                   for prediction in predictions {
                       if prediction.confidenceScore.prediction == .high &&
                           prediction.impact >= .medium &&
                           prediction.predictedInterval > QuantizedInterval.short {
                           self.prepareForDisruptiveWirelessEvent()
                       }
                   }
               }
           } catch {
               handlePredictionsError(error)
       }
   }

   private func prepareForDisruptiveWirelessEvent() {
       // Prepare for possible degradation of wireless connectivity
       // by caching more data now, temporarily increasing
       // retry count, or delaying network requests.
   }

   private func handlePredictionsError(_ error: Error) {
       // If error is .connectionError, consider waiting and then retrying
       // the loop over servicePredictions.
       // For other errors, such as .unsupportedDevice, don't expect the
       // ServicePredictionProvider to produce any predictions.
   }
}
```

## Topics

### Creating a service prediction provider
- [init()](servicepredictionprovider/init.md)
  Creates a service prediction provider.
### Receiving service predictions
- [var servicePredictions: any AsyncSequence<[ServicePrediction], any Error>](servicepredictionprovider/servicepredictions.md)
  An asychronous sequence of current predictions.
- [struct ServicePrediction](serviceprediction.md)
  An individual prediction of anticipated cellular network availability.
- [enum ServicePredictionError](servicepredictionerror.md)
  A type that represents errors encountered while using the WirelessInsights framework.

## See Also

- [Wireless Insights Service Predictions](../BundleResources/Entitlements/com.apple.developer.wireless-insights.service-predictions.md)
  A Boolean value that indicates whether the app can use the WirelessInsights framework to obtain wireless service predictions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wirelessinsights/servicepredictionprovider)*