import { on } from 'events';
import React from 'react';

interface ButtonProps {
  label: string;
  onClick: () => void;
}

export const Button: React.FC<ButtonProps> = ({ label, onClick }) => {
  return (
    <button
      // className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
      className="bg-gradient-to-r from-purple-500 to-indigo-500 hover:from-pink-500 hover:to-orange-500 text-white font-semibold py-2 px-4 border border-blue-500 rounded shadow"
      onClick={onClick}
    >
      {label}
    </button>
  );
};
