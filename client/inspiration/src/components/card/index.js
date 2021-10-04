import React from 'react';



const Card = ({info}) =>{
    if (info)console.log(info)
    else console.log("nothing here")
    return (
        <section>
        <div id="pic">
            <img src={info.pictureUrl} alt="emotional picture" />
            <p>{info.font_family}</p>
            <p>{info.font_weight}</p>
            <p>{info.font_style}</p>
            <p>{info.quote}</p>
        </div>
        </section>
    )
}

export default Card
