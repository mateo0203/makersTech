"use client";
import React, { useEffect, useRef, useState } from "react";
import { Box } from "@mui/material";
import Message from "./message";
import Input from "./input";
import { get } from "../api";

const defaultChat = [
  {
    id: 1,
    type: "bot",
    message: "Bienvenido al chat de Makers, en qué te puedo ayudar",
  },
  {
    id: 2,
    type: "user",
    message:
      "Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS",
  },
  {
    id: 3,
    type: "bot",
    message:
      "Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas?",
  },
  {
    id: 4,
    type: "bot",
    message: "Bienvenido al chat de Makers, en qué te puedo ayudar",
  },
  {
    id: 5,
    type: "user",
    message:
      "Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS",
  },
  {
    id: 6,
    type: "bot",
    message:
      "Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas?Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas?",
  },
  {
    id: 7,
    type: "bot",
    message: "Bienvenido al chat de Makers, en qué te puedo ayudar",
  },
  {
    id: 8,
    type: "user",
    message:
      "Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS",
  },
  {
    id: 9,
    type: "bot",
    message:
      "Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas?Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas?",
  },
  {
    id: 10,
    type: "bot",
    message: "Bienvenido al chat de Makers, en qué te puedo ayudar",
  },
  {
    id: 11,
    type: "user",
    message:
      "Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS Quiero saber cuantos computadores tienen de la marca ASUS",
  },
  {
    id: 12,
    type: "bot",
    message:
      "Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas?Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas? Tenemos 5 del año 2014 y 2 del 2025. Quieres saber algo mas?",
  },
];

//Componente principal para mostrar la ventana del chat
export default function ChatWindow() {
  const [chat, setChat] = useState(defaultChat);
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
    }
  };

  useEffect(() => {
    scrollToBottom();
  }, [chat]);

  const IAHelp = (text) => {
    setLoading(true); //para que el usuario no escriba mas
    get("/ia", {
      textUser: text,
    })
      .then((response) => {
        const newMessage = {
          id: Date.now() + 1,
          type: "bot",
          message: response,
        };
        setChat((prevMessages) => [...prevMessages, newMessage]);
        setLoading(false);
      })
      .catch((err) => {
        console.log(err);
        const newMessage = {
          id: Date.now() + 1,
          type: "bot",
          message: "Ha ocurrido un error, intente de nuevo",
        };
        setChat((prevMessages) => [...prevMessages, newMessage]);
        setLoading(false);
      });
  };

  const onKey = (text) => {
    const newMessage = { id: Date.now(), type: "user", message: text };
    setChat((prevMessages) => [...prevMessages, newMessage]);
    //llamar a IA con text user
    IAHelp(text);
  };

  return (
    <Box>
      <Box
        sx={{
          backgroundColor: "#e1f5fe",
          display: "flex",
          flexDirection: "column",
          height: "calc(100vh - 60px)",
          overflowY: "auto",
          paddingBottom: "20px",
        }}
      >
        {chat.map((message) => (
          <Message key={message.id} message={message} />
        ))}

        <div ref={messagesEndRef} />
      </Box>
      <Input onKey={onKey} loading={loading} />
    </Box>
  );
}
