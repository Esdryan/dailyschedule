/* eslint-disable no-unused-vars */
/* eslint-disable no-undef */
import PropTypes from 'prop-types';
<<<<<<< HEAD

const InputCriarCrono = ({type, name, id, onChange, value}) => {
	return (
		<div>
			<input
				type={type}
				name={name}
				id={id}
				onChange={onChange}
				value={value}
			/>{' '}
			<br />
		</div>
	);
};
=======

const InputCriarCrono = ({type, name, id, onChange, value}) => {
	return (
		<div>
			<input
				type={type}
				name={name}
				id={id}
				onChange={onChange}
				value={value}
			/>{' '}
			<br />
		</div>
	);
};

InputCriarCrono.propTypes = {
  type: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  id: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  value: PropTypes.string.isRequired,
};

>>>>>>> 92-testes-de-cobertura

InputCriarCrono.propTypes = {
  type: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  id: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  value: PropTypes.string.isRequired,
};


export default InputCriarCrono;