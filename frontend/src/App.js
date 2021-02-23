/* Import modules */
import React, { useState, useRef } from 'react';
import axios from 'axios';
/* Import CSS */
import './App.css';
/* Import utils */
import upload from './utils/upload.png';

/**
 * App - upload an image to digitalize
 */
function App() {
  /* Define the states for the app */
  const [FileName, setFileName] = useState("");
  const [UrlFile, setUrlFile] = useState("");
  const [DigitalizeN, setDigitalizeN] = useState(NaN);
  /* Define the references for the app */
  const hiddenFileInput = useRef(null);

  /**
   * customInputValue - set the reference to the input file
   * when click on "upload image" button. This is for customing 
   * the "upload image" button
   * @param {object} e event
   */
  const customInputValue = (e) => {
    hiddenFileInput.current.click();
  }

  /**
   * fileNameHandler - get the name of the file loaded
   * @param {object} e event
   */
  const fileNameHandler = (e) => {
    setFileName(e.target.files[0]);
    setUrlFile(URL.createObjectURL(e.target.files[0]));
    setDigitalizeN(NaN);
  }

  /**
   * uploadFileHandler - digitalize image
   */
  const uploadFileHandler = async () => {
    let res;
    const fd = new FormData();

    /*Add the image to body req*/
    fd.append('image', FileName, FileName.name);
    /*Make the request to digitalize the image*/
    res = await axios.post('http://localhost:5000/upload-image', fd);
    /*Save the response*/
    setDigitalizeN(res.data.Number_predicted);
  }

  return (
    <div className="App">
      {/* Display the image loaded to digitalize */}
      {UrlFile.length === 0 ?
        <img src={upload} onClick={customInputValue} alt="Upload" /> :
        <img className="frame_img" src={UrlFile} alt="Numbers" />}
      <br />
      {/* Button and input to load an image to app */}
      <button className="button button1" onClick={customInputValue}>
        Upload Image
      </button>
      <input type="file" onChange={fileNameHandler} ref={hiddenFileInput} style={{ display: 'none' }} />
      {/* Button to digitalize the image loaded */}
      <button className="button button2" onClick={uploadFileHandler}>
        Digitalize Image
      </button>
      <br />
      {/* Display what is the digitalize number of the image */}
      {isNaN(DigitalizeN) ? null : <p>The number in the image is {DigitalizeN}</p>}
    </div>
  );
}

export default App;
