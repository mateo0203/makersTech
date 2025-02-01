import Image from "next/image";
import styles from "./page.module.css";
import { Box, Container } from "@mui/material";
import Message from "./components/message";

const chat = [
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
];

export default function Home() {
  return (
    <Box>
      <Box
        sx={{
          backgroundColor: "#e1f5fe",
          display: "flex",
          flexDirection: "column",
        }}
      >
        {chat.map((message) => (
          <Message key={message.id} message={message}></Message>
        ))}
      </Box>
    </Box>
  );
}
