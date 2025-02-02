import { colors, Paper, TextField } from "@mui/material";
import React, { useState, useRef, useEffect } from "react";

// Input para que escriba el usuario
const Input = ({ onKey, loading }) => {
  const [text, setText] = useState("");

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && text.trim() !== "") {
      onKey(text);
      setText("");
    }
  };
  return (
    <TextField
      disabled={loading ? true : false} //evitar que escriba mientras la IA piensa
      fullWidth
      id="fullWidth"
      onKeyDown={handleKeyDown}
      onChange={(e) => setText(e.target.value)}
      value={text}
      placeholder="Escribe tu mensaje y presiona Enter..."
    />
  );
};

export default Input;
