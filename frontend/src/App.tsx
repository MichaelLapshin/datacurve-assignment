import { Button } from './components/Button';
import { MonacoEditor } from './components/MonacoEditor';
import axios from 'axios';
import { useRef, useEffect } from 'react';

function App() {
  const backendAddress = process.env.BACKEND_URL;
  const editorRef = useRef();

  // Button logic
  const handleTestCodeClick = async () => {
    console.log("Test code button clicked!");
    const code = editorRef.current.getValue();

    try {
      const response = await axios.post(`${backendAddress}/test-code`, {
        code: code
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleSubmitClick = async () => {
    console.log("Submit button clicked!");
    const code = editorRef.current.getValue();

    try {
      const response = await axios.post(`${backendAddress}/submit`, {
          code: code
      });
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  // Display basic web interface
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">
        Python Web Execution Environment
      </h1>
      <p className="text-sm mb-4">By Michael Lapshin</p>
      <div className="mb-4">
        {/* <Button label="Test Code" onClick={handleTestCodeClick}/> */}
        <Button label="Test Code" onClick={handleTestCodeClick}/>
        <Button label="Submit" onClick={handleSubmitClick}/>
      </div>
      <MonacoEditor ref={editorRef} />
      <div className="mb-4">
        {/* Program results go here */}
      </div>
    </div>
  );
}

export default App;