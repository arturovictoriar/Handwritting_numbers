import React, { useState, useRef } from 'react';
import './App.css';
import axios from 'axios';
import upload from './utils/upload.png';

function App() {
  const [FileName, setFileName] = useState("");
  const [UrlFile, setUrlFile] = useState("");
  const [DigitalizeN, setDigitalizeN] = useState(NaN);
  const hiddenFileInput = useRef(null);

  const customInputValue = (e) => {
    hiddenFileInput.current.click();
  }

  const fileNameHandler = (e) => {
    console.log(e.target.files[0]);
    setFileName(e.target.files[0]);
    setUrlFile(URL.createObjectURL(e.target.files[0]));
    setDigitalizeN(NaN);
  }

  const uploadFileHandler = async () => {
    let res;
    const fd = new FormData();
    fd.append('image', FileName, FileName.name);
    res = await axios.post('http://localhost:5000/upload-image', fd);
    console.log(res.data);
    setDigitalizeN(res.data.Number_predicted);
  }

  return (
    <div className="App">
      {UrlFile.length === 0 ?
        <img src={upload} onClick={customInputValue} alt="Upload" /> :
        <img src={UrlFile} alt="Numbers" />}
      <br />
      <button onClick={customInputValue}>Upload Image</button>
      <input type="file" onChange={fileNameHandler} ref={hiddenFileInput} style={{ display: 'none' }} />
      <button onClick={uploadFileHandler}>Digitalize Image</button>
      <br />
      {isNaN(DigitalizeN) ? null : <p>The number in the image is {DigitalizeN}</p>}
    </div>
  );
}

export default App;
