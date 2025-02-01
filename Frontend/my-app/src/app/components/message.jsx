import { colors, Paper } from "@mui/material";
import React from "react";

const Message = ({ message, key }) => {
  const backgroundColor = message.type === "bot" ? "#a5d6a7" : "white";
  const alignSelf = message.type === "bot" ? "flex-end" : "flex-start";
  return (
    <Paper
      sx={{
        backgroundColor: backgroundColor,
        padding: "10px",
        margin: "5px",
        borderRadius: "8px",
        display: "inline-block",
        maxWidth: "80%",
        alignSelf: alignSelf,
        whiteSpace: "normal",
        wordWrap: "break-word",
      }}
    >
      {message.message}
    </Paper>
  );
};

export default Message;
