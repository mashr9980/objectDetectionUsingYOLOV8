<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <h1>Automatic Number Plate Recognition System</h1>

  <p>
    This project is an <strong>Automatic Number Plate Recognition (ANPR)</strong> system developed using the 
    <a href="https://github.com/ultralytics/ultralytics">YOLOv8 framework</a>, which is a state-of-the-art object detection algorithm.
  </p>

  <h2>Key Features</h2>
  <ul>
    <li>Leverages the YOLOv8 model for high-performance object detection.</li>
    <li>Capable of detecting and localizing license plates in images.</li>
  </ul>

  <h2>Project Workflow</h2>
  <ol>
    <li><strong>Annotate Images:</strong> Use the <a href="https://github.com/tzutalin/labelImg">Label-IMG tool</a> to manually annotate license plates within your dataset.</li>
    <li><strong>Fine-tune YOLOv8:</strong> Fine-tune the YOLOv8 model using the annotated dataset to enable precise detection of number plates.</li>
    <li><strong>Prediction:</strong> After training, the model will be able to accurately identify and localize license plates in new images.</li>
  </ol>

  <h2>Technologies Used</h2>
  <ul>
    <li>YOLOv8 (You Only Look Once Version 8)</li>
    <li>Label-IMG tool for data annotation</li>
    <li>Python for model training and evaluation</li>
  </ul>

  <h2>How to Run</h2>
  <p>
    To run this project, clone the repository and follow the instructions below:
  </p>
  <pre>
    git clone https://github.com/mashr9980/ANPR-YOLOv8.git
    cd ANPR-YOLOv8
    # Setup the environment and run the detection script
    python app.py --source path_to_images
  </pre>

  <h2>Contributions</h2>
  <p>
    Contributions are welcome! Please submit a pull request or open an issue for any improvements.
  </p>

  <h2>License</h2>
  <p>
    This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.
  </p>

</body>
</html>
