import axios from 'axios';

export const loading = () => ({ type: 'LOADING'});

export const loadResult = ({ info} ) => ({ 
    type: 'LOAD_RESULT',
    payload: { info } 
});

export const getResult = ()=> {
    return async dispatch => {
        dispatch(loading());
        try {
            const newCard = getNewCard()
            dispatch(loadResult(newCard))
        } catch (err) {
            console.warn(err.message);
            dispatch({ type: 'SET_ERROR', payload: err.message })
        };
    };
};


export const getNewCard = () => {
    try {
        const data  = await axios.get(`http://127.0.0.1:8000/generator/`);
        return data;
    } catch(err) {
        if (data.status === 404) { throw Error('Try again pal!') }
        throw new Error(err.message)
    }
}