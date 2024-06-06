import React, { useEffect, useImperativeHandle, forwardRef  } from 'react';
import * as monaco from 'monaco-editor';
import axios from 'axios';

const MonacoEditor = forwardRef((props, ref) => {
  const editorRef = React.useRef();

  useImperativeHandle(ref, () => ({
    getValue: () => editorRef.current.getValue(),
  }));

  useEffect(() => {
    editorRef.current = monaco.editor.create(editorRef.current, {
      value: '# Welcome to Michael Lapshin\'s Datacurve assessment\nprint("Hello, World!");',
      language: 'python',
    });

    editorRef.current.onDidChangeModelContent(async () => {
      const code = editorRef.current.getValue();

      try {
        const response = await axios.post('https://api.judge0.com/submissions', {
          source_code: code,
          language_id: 71, // Python (3.8.1)
        });

        const result = await axios.get(`https://api.judge0.com/submissions/${response.data.token}`);

        if (result.data.stderr || result.data.compile_output) {
          // Display the error in the editor
          console.error(result.data.stderr || result.data.compile_output);
        }
      } catch (error) {
        console.error(error);
      }
    });
  }, []);

  return <div ref={editorRef} style={{ height: '400px' }} />;
});

export { MonacoEditor }; 
