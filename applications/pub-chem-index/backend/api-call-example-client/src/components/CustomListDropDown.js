import React from 'react'
export const CustomDropdown = (props) => (
  <div className="form-group">
    <select
      className="form-control"
      name="{syn}"
      onChange={props.onChange}
    >
      <option defaultValue>Select {props.name}</option>
      {props.options.map((item, index) => (
        <option key={index} value={item.id}>
          {item.name}
        </option>
      ))}
    </select>
  </div>
)
export default class CustomListDropDown extends React.Component {
  constructor() {
    super()
    this.state = {
      collection: [],
      selectedValue: '',
      value: '',
    }
  }
  handleSelectChange = (event) => {
    this.setState({ selectedValue: event.target.value })
  }
  handleInputChange = (event) => {
    this.setState({ value: event.target.value })
  }
  handleClick () {
    fetch(`/api/molecules/${this.state.value}`)
    .then(response => { return response.json() })
    .then((data) => {
      const options = data.map( item => { return { id : item[0], name: item[1] }})
      this.setState({ collection: options })
    })
    .catch((error) => {
      
    })
  }
  render() {
    return (
      <div className="container mt-4">
        <h2>Pubchem search sample React app</h2>
        <input value={this.state.value} onChange={(e) => {this.handleInputChange(e)}} />
        <button onClick={this.handleClick.bind(this)}>Search</button>
        <CustomDropdown
          options={this.state.collection}
          onChange={this.handleSelectChange}
        />
      </div>
    )
  }
}