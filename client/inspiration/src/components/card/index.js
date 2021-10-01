import React from 'react';
import './style.css';

const Card = ({ info }) =>{
    return (
        <section>
        <div id="pic">
            <img src={info.pictureUrl} alt="emotional picture" />
            <p>{info.fontFamily}</p>
            <p>{info.fontWeight}</p>
            <p>{info.fontStyle}</p>
            
        </div>
        </section>
    )
}

export default Card
