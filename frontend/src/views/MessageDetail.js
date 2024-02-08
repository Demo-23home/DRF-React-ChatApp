import React from "react";
import "./style/message.css";
import { useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";
import useAxios from "../utils/useAxios";
import moment from 'moment'
import { useParams } from "react-router-dom";

const MessageDetail = () => {

    const baseURL = 'http://localhost:8000/messages/'
    const [messages, setMessages] = useState([])

    const id = useParams()
    const axios = useAxios()
    const token = localStorage.getItem("authTokens")
    const decoded = jwtDecode(token)
    const reciever_id = decoded.user_id
    
    // console.log(reciever_id);
    // console.log(id)
    
 
    useEffect(() => {
        try{
         axios.get(baseURL + 'get-messages/' + id.id + '/' + reciever_id + '/').then((res) => {
            console.log(res.data)
            setMessages(res.data)
         })

        } catch(error){
            console.log(error)
        }
    }, [])    
 
    return (
    <div>MessageDetail</div>
  )
}

export default MessageDetail