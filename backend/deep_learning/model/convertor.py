import tensorflow as tf

print("Loading original 233MB model...")
trained_model = tf.keras.models.load_model('Signature_verify_model.h5')

print("Slicing model to create feature extractor...")
feature_extractor = tf.keras.models.Model(
    inputs=trained_model.input, 
    outputs=trained_model.layers[-8].output
)

print("Setting up TFLite Converter...")
converter = tf.lite.TFLiteConverter.from_keras_model(feature_extractor)

# Turn on default optimizations
converter.optimizations = [tf.lite.Optimize.DEFAULT]
# Force the optimization to use Float16 (Half Precision)
converter.target_spec.supported_types = [tf.float16]

print("Converting to Float16 TFLite (This might take a minute)...")
tflite_model = converter.convert()

print("Saving feature_extractor.tflite...")
with open('feature_extractor.tflite', 'wb') as f:
    f.write(tflite_model)

print("Done")