import React from 'react'
export const CustomDropdown = (props) => (
  <div className="form-group">
    <select
      className="form-control"
      name="{props.username}"
      onChange={props.onChange}
    >
      <option defaultValue>Select {props.name}</option>
      {props.options.map((item, index) => (
        <option key={index} value={item.id}>
          {item.username}
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
    fetch(`https://pubchem.olfactory.dev.metacell.us/molecules/${this.state.value}`)
    .then((response) => { response.json() })
    .then((res) => this.setState({ collection: res }))
    var event = new Event('input', { bubbles: true });
    this.myinput.dispatchEvent(event);
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