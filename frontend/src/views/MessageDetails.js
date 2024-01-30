import React from "react";
import "./style/message.css";
import { useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";
import useAxios from "../utils/useAxios";
import moment from 'moment'



import React from 'react'

const MessageDetails = () => {
    const baseURL = 'http://localhost:8000/messages'
  return (
    <div>MessageDetails</div>
  )
}

export default MessageDetails